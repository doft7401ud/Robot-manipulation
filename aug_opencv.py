import cv2
import numpy as np
import random
import os

dishDir = r'C:\Users\goodb\Desktop\PythonPractice\aaa1230\test_result\Photos'


for k in os.listdir(dishDir):
    
    for j in os.listdir('C:\\Users\\goodb\\Desktop\\PythonPractice\\aaa1230\\test_result\\Photos\\' + k):
    # Load the image
        while(True):
            ran_num_list=[random.randrange(2) for i in range(7)]
            if 1 in ran_num_list:
                break
        print(ran_num_list)
        for i in range(10):
            image = cv2.imread("C:\\Users\\goodb\\Desktop\\PythonPractice\\aaa1230\\test_result\\Photos\\"+k+"\\"+j)
            if ran_num_list[0]==1: # 回転
                M = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), random.randrange(360), 1)
                # Apply the transformation
                image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
            if ran_num_list[1]==1: # 左右反転
                image = np.fliplr(image)
            if ran_num_list[2]==1: # 上下反転
                image = np.flipud(image)
                
            if ran_num_list[3]==1: # noise    
                row,col,ch = image.shape
                noize_degree=random.randint(1,3)
                # 白
                pts_x = np.random.randint(0, col-1 ,noize_degree*1000000) #0から(col-1)までの乱数を千個作る
                pts_y = np.random.randint(0, row-1 , noize_degree*1000000)
                image[(pts_y,pts_x)] = (255,255,255) #y,xの順番になることに注意
                # 黒
                pts_x = np.random.randint(0, col-1 , noize_degree*1000000)
                pts_y = np.random.randint(0, row-1 , noize_degree*1000000)
                image[(pts_y,pts_x)] = (0,0,0)
             
            if ran_num_list[4]==1:
                continue
                # 拡大縮小
            # 元画像4096*3072
            
            if ran_num_list[5]==1:
                # 明るさ
                image = cv2.convertScaleAbs(image,alpha = (random.randint(5,15))/10,beta = random.randint(-50,50))
            if ran_num_list[6]==1:
                # ぼかしバンバンジー豆腐
                how_blur=random.randint(2,8)*10
                image = cv2.blur(image, (how_blur, how_blur))
        # Define the transformation
    # 保存
            cv2.imwrite(("C:\\Users\\goodb\\Desktop\\PythonPractice\\aaa1230\\test_result\\Photos\\"+k+"\\"+j).strip(".jpg")+"_augmented_"+f"{i}.jpg",image)