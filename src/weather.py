#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/6/1
# Time: 11:16
import requests

WEATHER_API = 'https://free-api.heweather.com/v5/weather?&key=29d118a3de6a4ca284f91c59ad28db0f&city='


def message(args):
    city = args['city']
    r = requests.get(WEATHER_API+city)
    j = r.json()

    if r.status_code == 200 and j["HeWeather5"][0]["status"] == "ok":
        max_tmp = j["HeWeather5"][0]['daily_forecast'][0]['tmp']['max']
        min_tmp = j["HeWeather5"][0]['daily_forecast'][0]['tmp']['min']
        cond_day = j["HeWeather5"][0]['daily_forecast'][0]['cond']['txt_d']
        cond_night = j["HeWeather5"][0]['daily_forecast'][0]['cond']['txt_n']
        aqi = j["HeWeather5"][0]['aqi']['city']['qlty']

        text = u"今天天气\n" \
               u"最高 : %s 度\n" \
               u"最低 : %s 度\n" \
               u"白天 : %s\n" \
               u"夜晚 : %s\n" \
               u"空气质量 : %s" \
               % (max_tmp, min_tmp, cond_day, cond_night, aqi)
        return text

    else:
        return u"获取天气失败了"

if __name__ == '__main__':
    message({'city': 'shanghai'})
