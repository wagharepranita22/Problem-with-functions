# formula  height * width % cover can
def pain_area_calculator(height , width,cover_can):
    area=height*width
    paint_area=area//cover_can
    print(f"Cover paint area :{paint_area}")

height,width,cover_can=map(int,input("Give your inputs of height width cover : ").split())
pain_area_calculator(height,width,cover_can)

