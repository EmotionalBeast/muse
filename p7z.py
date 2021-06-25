# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2021/06/25 18:08

from py7zr import unpack_7zarchive, pack_7zarchive
import shutil

'''
# register file format at first.
shutil.register_archive_format('7zip', pack_7zarchive, description='7zip archive')
shutil.register_unpack_format('7zip', ['.7z'], unpack_7zarchive)

# extraction
shutil.unpack_archive('./workspace/10432.7z', './')

# compression
shutil.make_archive('./10433', '7zip', './workspace/10433')
# make_archive('文件名前缀', '压缩格式', '需要压缩的文件或文件夹')
'''


class SevenZip(object):

    def __init__(self):
        shutil.register_archive_format('7zip', pack_7zarchive, description='7zip archive')
        shutil.register_unpack_format('7zip', ['.7z'], unpack_7zarchive)

    def unpack(self, src, target):
        shutil.unpack_archive(src, target)

    def pack(self, src, target):
        shutil.make_archive(src, "7zip", target)