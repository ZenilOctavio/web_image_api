FROM python:latest

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

# Install playwright-python
RUN pip install playwright

# Download the browser binaries for Playwright
RUN playwright install-deps
RUN playwright install

EXPOSE 8000
CMD ["uvicorn","server:app","--host","0.0.0.0","--port","8000"]
