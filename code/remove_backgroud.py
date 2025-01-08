# 2025-01-08 by goodwvn

from rembg import remove, new_session
from PIL import Image
from path import test_pic_path

def remove_background(input_path, output_path, model_name=''):
    """
    移除图片背景并保存为PNG
    
    参数:
        input_path: 输入图片路径
        output_path: 输出图片路径(PNG格式)
    返回:
        bool: 处理成功返回True
    """
    try:
        session = new_session(model_name)

        # 读取输入图片
        input_image = Image.open(input_path)
        
        # 移除背景
        output_image = remove(input_image, session=None)
        
        # 保存结果
        output_image.save(output_path, format='PNG')
        return True
        
    except Exception as e:
        print(f"背景移除失败: {str(e)}")
        return False


remove_background(test_pic_path, 'dataset\\test\\1_nobg.png', model_name='u2netp')
