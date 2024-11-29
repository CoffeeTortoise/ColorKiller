from PIL import Image
import os
from config import FORMATS


class Remover:
    
    @staticmethod
    def remove_color(source: str,
                     res: str,
                     is_file: bool,
                     color: tuple[int, int, int],
                     rm_source: bool = True) -> None:
        if is_file:
            if not any([source.endswith(ext) for ext in FORMATS]):
                return
            Remover.proc_file(source, res, color, rm_source)
            return
        for file in os.listdir(source):
            if not any([file.endswith(ext) for ext in FORMATS]):
                continue
            src_path: str = f'{source}/{file}'
            res_file: str = file.replace('jpeg', 'png') if file.endswith('jpeg') else file.replace(file[-3:], 'png')
            res_path: str = f'{res}/{res_file}'
            Remover.proc_file(src_path, res_path, color, rm_source)  
    
    @staticmethod
    def proc_file(source: str,
                  res: str,
                  color: tuple[int, int, int],
                  rm_source: bool = True) -> None:
        if source.endswith('.png'):
            src: str = source
            is_png: bool = True
        else:
            src: str = Remover.convert(source, rm_source)
            is_png: bool = False
        image = Image.open(src)
        img = image.convert('RGBA')
        datas = img.getdata()
        new_data = []
        for item in datas:
            if (item[0], item[1], item[2]) == color:
                new_data.append((color[0], color[1], color[2], 0))
            else:
                new_data.append(item)
        img.putdata(new_data)
        image.close()
        if not is_png:
            os.remove(src)
        img.save(res, format='png')
    
    @staticmethod
    def convert(source: str, 
                rm_source: bool = True) -> str:
        check: list[bool] = [source.endswith(ext) for ext in FORMATS]
        ind: int = check.index(True)
        new: str = source.replace(FORMATS[ind], '.png')
        with Image.open(source) as image:
            image.save(new, format='png')
        if rm_source:
            os.remove(source)
        return new
