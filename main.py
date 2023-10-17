from WebImageCreator.component_retriever import ComponentRetriever

retriever = ComponentRetriever('./components')
components = retriever.read_components()

print(components)

