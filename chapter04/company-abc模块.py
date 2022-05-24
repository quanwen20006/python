#!usr/bin/env python
# -*- coding:utf-8 -*-

"""
抽象基类--子类必须实现到父类到某些方法，类似于Java的接口

1 ：基类必须实现abc类
2 ：方法必须被abc里面到abstractmethod修饰
3 ：子类至少全部实现被abstractmethod修饰的函数
"""
import abc


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase):
    def __init__(self):
        print('RedisCache init...')

    def get(self, key):
        pass

    def set(self, key, value):
        pass


redis = RedisCache()
