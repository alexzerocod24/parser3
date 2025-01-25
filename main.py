from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import wikipediaapi

import time

def search_wikipedia(query):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(query)
    if page.exists():
        return page
    else:
        return None

def list_paragraphs(page):
    print("\nParagraphs:\n")
    for section in page.sections:
        print(section.title)
        print(section.text[:200] + "...\n")

def list_links(page):
    print("\nLinks:\n")
    links = list(page.links.keys())
    for i, link in enumerate(links):
        print(f"{i+1}: {link}")
    return links

def main():
    query = input(" Введите запрос для поиска :")
    page = search_wikipedia(query)

    if not page:
        print("Страница по запросу не найдена.")
        return

    while True:
        print("\nChoose an action:")
        print("1. Просмотр абзацев текущей статьи.")
        print("2. Перейти на нужную страницу.")
        print("3. Выход.")

        choice = input("Введите выбранное действие (1/2/3): ")

        if choice == '1':
            list_paragraphs(page)
        elif choice == '2':
            links = list_links(page)
            link_choice = int(input(f"Введите номер ссылки, по которой будет переход (1-{len(links)}): ")) - 1
            if 0 <= link_choice < len(links):
                new_query = links[link_choice]
                page = search_wikipedia(new_query)
                if not page:
                    print("Страница по запросу не найдена.")
            else:
                print("Ошибочный выбор.")
        elif choice == '3':
            break
        else:
            print("Ошибочный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
