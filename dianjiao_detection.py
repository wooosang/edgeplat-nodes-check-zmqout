
import cv2
# import time,os

def threshold_method(img,lowval = 64):

    # img = cv2.imread(img,0)
    # cv2.imshow("old_img", img)
    img = cv2.GaussianBlur(img, (5, 5), 0)

    # edge_output = cv2.Canny(img, 10, 35)
    # cv2.imshow("Canny_img", edge_output)

    # th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 7, 3)
    # cv2.imshow("adapt_img", th2)

    t, rst=cv2.threshold(img,lowval,255, cv2.THRESH_BINARY_INV)
    # t, rst = cv2.threshold(img, 91, 255, cv2.THRESH_BINARY_INV)

    # print(rst)
    # rst1 = rst[:,140:200]
    # rst2 = rst[:,200:260]
    # cv2.imshow("rst1", rst1)
    # cv2.imshow("rst2", rst2)

    # l1 = rst[0:5,140:200]
    # print(len(l1[l1==0]))
    # print(rst1.shape)

    # cv2.imshow("img", img)
    # cv2.imshow("rst", rst)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    return rst

def statistics_width(img,height = 30 ,step = 5):
    result = []

    for i in range(0, img.shape[0] - height + 1, step):
        img_chapter = img[i:i+height,:]
        rst = len(img_chapter[img_chapter==0])//height
        result.append(rst)

    return result

def detection(img,lowval = 64,height = 30,step = 5,alarm_lowval = 4 ,alarm_highval = 22,warn_lowval = 7,warn_highval = 17):
    result = []

    rst = threshold_method(img[:,:,0],lowval)

    result1 = statistics_width(rst[:,140:200],height,step)
    result2 = statistics_width(rst[:,200:260],height,step)

    for i in range(len(result1)):
        if (result1[i] <= alarm_lowval or result1[i] >= alarm_highval) and (result2[i] <= alarm_lowval or result2[i] >= alarm_highval):
            result.append(4)
        elif (result1[i] <= alarm_lowval or result1[i] >= alarm_highval) or (result2[i] <= alarm_lowval or result2[i] >= alarm_highval):
            result.append(3)
        elif (alarm_lowval < result1[i] <= warn_lowval or warn_highval <= result1[i] < alarm_highval) \
                and (alarm_lowval < result2[i] <= warn_lowval or warn_highval <= result2[i] < alarm_highval):
            result.append(2)
        elif (alarm_lowval < result1[i] <= warn_lowval or warn_highval <= result1[i] < alarm_highval) \
                or (alarm_lowval < result2[i] <= warn_lowval or warn_highval <= result2[i] < alarm_highval):
            result.append(1)
        else:
            result.append(0)

    print(result)
    return max(result)


# if __name__ == '__main__':
#     path = "C:/Users/12171\Desktop/1"
#     for i in os.listdir(path):
#         start = time.time()
#         img_path = os.path.join(path,i)
#
#         img = cv2.imread(img_path)
#
#         # print(img[:,:,0])
#
#         result = detection(img)
#         print(result)
#
#         # rst = threshold_method(img[:,:,0])
#
#         # result1 = statistics_width(rst[:,140:200])
#         # result2 = statistics_width(rst[:, 200:260])
#         # print(result1)
#         # print(result2)
#
#
#
#         end = time.time()
#         print(end-start)
#         break


