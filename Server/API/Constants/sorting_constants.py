class Sorting:
    sorting_from_low = {
        "filter": {
            "productStock": {
                "$gt": 0
            }
        },
        "sort": {
            "price": 1
        },
        "lookup": False,
        "limit": 50,
        "user": False,
        "info": {
            "lng": "hebrew",
            "platform": "web",
            "screenHeight": 864,
            "screenWidth": 1536,
            "location": {
                "ancestorOrigins": {},
                "href": "https://qa.trado.co.il/?&sort={%22price%22:1}",
                "origin": "https://qa.trado.co.il",
                "protocol": "https:",
                "host": "qa.trado.co.il",
                "hostname": "qa.trado.co.il",
                "port": "",
                "pathname": "/",
                "search": "?&sort={%22price%22:1}",
                "hash": ""
            }
        }
        }

    sorting_from_hp = {
        "filter": {
            "productStock": {
                "$gt": 0
            }
        },
        "sort": {
            "price": -1
        },
        "lookup": False,
        "limit": 50,
        "user": False,
        "info": {
            "lng": "hebrew",
            "platform": "web",
            "screenHeight": 864,
            "screenWidth": 1536,
            "location": {
                "ancestorOrigins": {},
                "href": "https://qa.trado.co.il/?&sort={%22price%22:-1}",
                "origin": "https://qa.trado.co.il",
                "protocol": "https:",
                "host": "qa.trado.co.il",
                "hostname": "qa.trado.co.il",
                "port": "",
                "pathname": "/",
                "search": "?&sort={%22price%22:-1}",
                "hash": ""
            }
        }
    }

    searching_kevin = {
        "search": "קווין ג'קי",
        "info": {
            "lng": "hebrew",
            "platform": "web",
            "screenHeight": 864,
            "screenWidth": 1536,
            "location": {
                "ancestorOrigins": {},
                "href": "https://qa.trado.co.il/?&sort={%22price%22:-1}",
                "origin": "https://qa.trado.co.il",
                "protocol": "https:",
                "host": "qa.trado.co.il",
                "hostname": "qa.trado.co.il",
                "port": "",
                "pathname": "/",
                "search": "?&sort={%22price%22:-1}",
                "hash": ""
            }
        }
    }

    snack_link = {
        "filter": {
            "sectionName": "חטיפים",
            "productStock": {
                "$gt": 0
            }
        },
        "lookup": False,
        "limit": 50,
        "isSaleSection": "חטיפים",
        "user": False,
        "info": {
            "lng": "hebrew",
            "platform": "web",
            "screenHeight": 864,
            "screenWidth": 1536,
            "location": {
                "ancestorOrigins": {},
                "href": "https://qa.trado.co.il/?sectionName=%D7%97%D7%98%D7%99%D7%A4%D7%99%D7%9D",
                "origin": "https://qa.trado.co.il",
                "protocol": "https:",
                "host": "qa.trado.co.il",
                "hostname": "qa.trado.co.il",
                "port": "",
                "pathname": "/",
                "search": "?sectionName=%D7%97%D7%98%D7%99%D7%A4%D7%99%D7%9D",
                "hash": ""
            }
        }
    }

    gorilla_glu = {
        "filter": {
            "barcode": "35058"
        },
        "dataOnly": True,
        "limit": 1,
        "full": True,
        "info": {
            "lng": "hebrew",
            "platform": "web",
            "screenHeight": 864,
            "screenWidth": 1536,
            "location": {
                "ancestorOrigins": {},
                "href": "https://qa.trado.co.il/product/35058",
                "origin": "https://qa.trado.co.il",
                "protocol": "https:",
                "host": "qa.trado.co.il",
                "hostname": "qa.trado.co.il",
                "port": "",
                "pathname": "/product/35058",
                "search": "",
                "hash": ""
            }
        }
    }

    filter_by_letter_g = {
        "search": "ג",
        "info": {
            "lng": "hebrew",
            "platform": "web",
            "screenHeight": 864,
            "screenWidth": 1536,
            "location": {
                "ancestorOrigins": {},
                "href": "https://qa.trado.co.il/?sectionName=%D7%9E%D7%A9%D7%A7%D7%90%D7%95%D7%AA",
                "origin": "https://qa.trado.co.il",
                "protocol": "https:",
                "host": "qa.trado.co.il",
                "hostname": "qa.trado.co.il",
                "port": "",
                "pathname": "/",
                "search": "?sectionName=%D7%9E%D7%A9%D7%A7%D7%90%D7%95%D7%AA",
                "hash": ""
            }
        }
    }

    snacks_url = "https://qa.trado.co.il/api/product/filter"
    sorting_lp_url = "https://qa.trado.co.il/api/product/filter"
    sorting_hp_url = "https://qa.trado.co.il/api/product/filter"
    searching_kevin_url = "https://qa.trado.co.il/api/product/filter"
    gorilla_glu_url = "https://qa.trado.co.il/api/product/filter"
    filter_withg_url = "https://qa.trado.co.il/api/product/filter"
