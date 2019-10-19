import requests
import pprint
import wget
from PIL import Image


#my_cats = requests.get('https://api.thecatapi.com/v1/breeds?page=2&limit=1')

def get_breeds_name(my_cats):
    
    new_cats = dict()

    for json in my_cats.json():
        for key, value in json.items():
            if key  == 'name':
                new_cats[key] = value
            if  key == 'temperament':
                new_cats[key] = value
            if key == 'id':
                new_cats[key] = value
    print(new_cats)
    return new_cats

def get_new_cat_img(my_cat):
    print(my_cat['id'])
    new_cat = requests.get('https://api.thecatapi.com/v1/images/search?breed_id={0}'.format( my_cat['id']) )
    
    kitty_dict = dict()

    for json in new_cat.json():
        for key, value in json.items():
            if key =='url':
                kitty_dict[key] = value
    
    kitty_dict['name'] = my_cat['name']

    print(kitty_dict)
    return kitty_dict



def show_me_the_kitty(kitty):
       
    files = []
    
    old_name = kitty['name'].split()
    cat_name = '_'.join(old_name)

    with open(cat_name+'.jpg', 'wb') as jpg_file:
            cat_img = requests.get(kitty['url'])
            jpg_file.write(cat_img.content)
            files.append(kitty['name']+'.jpg' )
    
    return files

def open_cats(cats):

    for cat in cats:
        Image.open(cat)

def main():

    my_cats = requests.get('https://api.thecatapi.com/v1/breeds?page=2&limit=1')
    cat = get_breeds_name(my_cats)
    cat_url = get_new_cat_img(cat)
    cat_files =show_me_the_kitty(cat_url )
    open_cats( cat_files )

if __name__=="__main__":
    main()
