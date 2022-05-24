#!/usr/bin/python3
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         类方法
# Description:  
# Author:       quanwen
# Date:         2019/10/16
# -------------------------------------------------------------------------------
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def check_valid(date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year) > 0 and ((int(month)) > 0 and int(month) <= 12) and (int(day) > 0 and int(day) < 32):
            return True
        else:
            return False

    @classmethod
    def parse_date_str(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)


if __name__ == '__main__':
    new_day = Date(2019, 10, 16)
    print("new_day ", new_day)

    # 使用staticmethod方法初始化
    print("check ", Date.check_valid("2019-11-33"))

    # 使用classmethod方法初始化
    new_day = Date.parse_date_str("2019-10-19")
    print("new_day ", new_day)
