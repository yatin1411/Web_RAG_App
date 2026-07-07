from app.cleaner.cleaner import clean_markdown
from app.cleaner.storage import load_pages, save_pages


def main():

    pages = load_pages()

    print(f"Loaded {len(pages)} pages")

    for page in pages:

        page.markdown = clean_markdown(page.markdown)

    save_pages(pages)

    print("Cleaning completed.")
    print("Saved to data/cleaned/pages.json")


if __name__ == "__main__":
    main()