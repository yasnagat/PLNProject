import spacy

# funcao de abertura do arquivo
def read_archive(d_archive_name):
    with open(d_archive_name, encoding="utf8") as archive_content:
        content = archive_content.read()
    return content

# funcao que retira as stopwords e retorna o conteudo em formato de string/texto
def clear_content(d_initial_content):
    lib = spacy.load("pt_core_news_lg")
    content = lib(d_initial_content)
    cleared_content = ' '.join([token.text for token in content if not token.is_stop and not token.is_punct or token.is_bracket])

    return cleared_content

# funcao que tokeniza o conteudo do texto por sentencas
def tokenize_content(d_cleared_content):
    lib = spacy.load("pt_core_news_lg")
    content = lib(d_cleared_content)
    list_sentences = [sentence for sentence in content.sents]
    return list_sentences

# funcao que determina a similaridade entre as sentencas do texto
def semantic_similarity(d_list_sentences):
    cont = 0
    for i in range (0, len(d_list_sentences) - 1):
        print("-----------", i, "----------------")

        calc_similarity = d_list_sentences[i].similarity(d_list_sentences[i+1])
        cont += 1
        print("Primeira sentença: ", d_list_sentences[i])
        print("Segunda sentença: ", d_list_sentences[i+1])

        print("Similaridade: ",calc_similarity)
    print(cont)


# main program
print("""NLP EXTRACTOR INITIALIZED...
-------------------------------------------------------------- 
Insert the archive's name you want to obtain the data. 
Don't forget to add the archive's format in your input.
""")

initial_content = read_archive(input("Name (name.format): "))

content_cleared = clear_content(initial_content)

list_content = tokenize_content(content_cleared)

semantic_similarity(list_content)