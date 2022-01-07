from PIL import Image

a = list(input())
# 1. 병합 이미지 만들기
merged = Image.new('L', (200*len(a), 120))

# 2. 이미지 불러오기
for i in range(a):
    im = Image.open('mnist_' + str(5 * i) + '.png')

    # 3. 이미지 붙여넣기
    merged.paste(im, (200*len(a), 120))

# 4. 병합한 이미지 저장하기
merged.save('./new_Braille/merged.png')