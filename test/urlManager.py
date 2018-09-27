"""
 Created by yan on 2018/9/25 18:07
"""
__author__ = 'yan'



class UrlManager(object):
    """
    连接管理器
    """
    @staticmethod
    def buildUrl(path):
        """
        没有做任何处理，直接返回路由
        :param path:
        :return:
        """
        return path

    @staticmethod
    def buildStaticUrl(path):
        """
        返回带版本的路由，version可以通过动态传递进行动态的改变
        :param path:
        :return:
        """
        path = path+'?version=20180925'
        return UrlManager.buildUrl(path)
