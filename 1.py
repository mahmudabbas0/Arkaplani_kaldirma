from rembg import remove 
import requests
from PIL import Image
from io import BytesIO
import os 




os.makedirs('original' , exist_ok=True)
os.makedirs('masked' , exist_ok=True)


img_url ='https://www.horsejournals.com/files/pictures-videos/articles/shutterstock_733256173_-_rita_kochmarjova-mainweb.jpg'
img_name = img_url.split('/')[-1]


img = Image.open(BytesIO(requests.get(img_url).content))
img.save('original/' + img_name ,format= 'jpeg')


output_path = 'masked/' + img_name


with open(output_path,'wb') as f:
    input = open('original/' + img_name,'rb').read()
    subject = remove(input,alpha_matting=True)
    f.write(subject)
    
    
    
# backgroung_img ='https://i.pinimg.com/originals/19/ab/ce/19abcecfcba03df5eb748b19df29be76.jpg'
# backgroung_img = Image.open(BytesIO(requests.get(backgroung_img).content))

# backgroung_img= backgroung_img.resize((img.width,img.height))

# foreground_img = Image.open(output_path)
# backgroung_img.paste(foreground_img,(0,0),foreground_img)
# backgroung_img.save('masked/' + img_name ,format= 'jpeg')