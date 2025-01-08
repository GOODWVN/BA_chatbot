# 2025-01-08 by goodwvn
from path import test_pic_path

import cv2
import numpy as np

def detect_edges_multiple(image_path, method='canny'):
    """
    参数:
        image_path: 图像路径
        method: 'sobel', 'laplacian', 'scharr', 'canny'
    """
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    if method == 'sobel':
        # Sobel算子
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        edges = cv2.magnitude(sobelx, sobely)
        
    elif method == 'laplacian':
        # Laplacian算子
        edges = cv2.Laplacian(gray, cv2.CV_64F)
        
    elif method == 'scharr':
        # Scharr算子
        scharrx = cv2.Scharr(gray, cv2.CV_64F, 1, 0)
        scharry = cv2.Scharr(gray, cv2.CV_64F, 0, 1)
        edges = cv2.magnitude(scharrx, scharry)
        
    else:
        # 默认使用Canny
        edges = cv2.Canny(gray, 200, 380)
    
    # 转换为二值图像
    edges = np.uint8(np.absolute(edges))
    _, edges = cv2.threshold(edges, 50, 255, cv2.THRESH_BINARY)
    
    # 获取边缘坐标
    edge_coordinates = np.where(edges != 0)
    edge_points = list(zip(edge_coordinates[1], edge_coordinates[0]))
    
    return edge_points


def label_edges(image_path, output_path, color=(0, 255, 0), thickness=1):
    """
    参数:
        image_path: 输入图像路径
        output_path: 输出图像路径
        color: 边缘标注颜色，默认绿色 (B,G,R)
        thickness: 边缘点绘制粗细
    """
    # 读取原图
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("无法读取图像")
    
    # 获取边缘坐标
    edge_points = detect_edges_multiple(image_path, method='canny')
    
    
    # 在图像上标注边缘点
    for point in edge_points:
        x, y = point
        cv2.circle(img, (x, y), radius=thickness, color=color, thickness=-1)
    
    # 保存结果
    cv2.imwrite(output_path, img)
    return True


label_edges('dataset\\test\\1_nobg.png', 'dataset\\test\\1_nobg_labeled.png')
