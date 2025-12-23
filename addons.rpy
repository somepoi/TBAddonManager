init python:
    class Addon:
        def __init__(self, label, name, description="", avatar=None, authors=None):
            self.label = label
            self.name = name
            self.description = description
            self.avatar = avatar
            if authors is None:
                self.authors = []
            elif isinstance(authors, str):
                self.authors = [authors] if authors else []
            elif isinstance(authors, list):
                self.authors = authors
            else:
                self.authors = []
        
        def __repr__(self):
            return f"Addon({self.name})"
        
        def get_truncated_name(self, max_length=60):
            if len(self.name) > max_length:
                return self.name[:max_length] + "..."
            return self.name
        
        def get_adaptive_name_size(self):
            length = len(self.name)
            if length <= 20:
                return 80
            elif length <= 30:
                return 60
            elif length <= 40:
                return 50
            elif length <= 50:
                return 40
            else:
                return 35
        
        def get_authors(self):
            if not self.authors:
                return ""
            elif len(self.authors) == 1:
                return self.authors[0]
            else:
                return ", ".join(self.authors)
        
        def matches_search(self, search_query):
            if not search_query:
                return True
            
            search_query = latinify(search_query)

            query_lower = search_query.lower()
        
            # Название
            if query_lower in latinify(self.name.lower()) or search_query in latinify(self.name):
                return True
            
            # Описание
            if query_lower in latinify(self.description.lower()) or search_query in latinify(self.description):
                return True
            
            # Авторы
            for author in self.authors:
                if query_lower in latinify(author.lower()) or search_query in latinify(author):
                    return True
            
            return False
    
    addons = {}
    
    # Переменная для выбранного мода (для показа деталей)
    selected_addon = None
    
    # Сортировка (False = A-Z, True = Z-A)
    addon_sort_reverse = False
    
    # Поисковой запрос
    addon_search_query = ""

    cyr_chars = "йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ\"№;:?"
    lat_chars = "qwertyuiop[]asdfghjkl;'zxcvbnm,.QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>@#$^&"

    def latinify(s: str):
        return s.translate(str.maketrans(cyr_chars, lat_chars))

    def delatinify(s: str):
        return s.translate(str.maketrans(lat_chars, cyr_chars))

    def get_sorted_addons():
        return sorted(addons.items(), key=lambda x: x[1].name, reverse=addon_sort_reverse)
    
    def get_filtered_addons():
        filtered = [(label, addon) for label, addon in addons.items() 
                    if addon.matches_search(addon_search_query)]
        return sorted(filtered, key=lambda x: x[1].name, reverse=addon_sort_reverse)
    
    def toggle_addon_sort():
        global addon_sort_reverse
        addon_sort_reverse = not addon_sort_reverse
