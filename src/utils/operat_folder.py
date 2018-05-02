import os


class folders():
    def get_all_folders(self):
        """获取电脑中所有的文件夹"""
        for folders in os.listdir("."):
            if os.path.isdir(folders):
                self.get_all_folders(folders)

    async def filter_folders_has_pictures(self):
        """获取所有含有图片的文件夹"""
        return

    async def get_all_pictures(self):
        """获取文件夹中的所有图片文件"""
        return
