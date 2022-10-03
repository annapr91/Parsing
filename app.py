from parsing.data import Books,ChildsGames,Apps, Games


def main():
    info_books=Books('https://play.google.com/store/books?hl=ru')
    info_books.get_text()
    info_books.get_data()
    info_books.save_data('list_books.json')

    info_child_games=ChildsGames('https://play.google.com/store/apps/category/FAMILY?hl=ru')
    info_child_games.get_text()
    info_child_games.get_data()
    info_child_games.save_data('list_child.json')

    info_app = Apps('https://play.google.com/store/apps?hl=ru')
    info_app.get_text()
    info_app.get_data()
    info_app.save_data('list_apps.json')

    info_games = Games('https://play.google.com/store/games?hl=ru')
    info_games.get_text()
    info_games.get_data()
    info_games.save_data('list_games.json')






if __name__ == "__main__":
    main()
