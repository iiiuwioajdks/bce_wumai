package com.threeonetwo.weatherservice.service.impl;

import com.alibaba.fastjson.JSONObject;
import com.threeonetwo.weatherservice.service.WeatherService;
import com.threeonetwo.weatherservice.utils.ResultJson;
import com.threeonetwo.weatherservice.utils.WeatherAPI;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @Class: WeatherServiceImpl
 * @Author: Wei Junwei
 * @Time: 21:40 2022/5/6
 * @XiDianUniversity
 * @Description:
 */
@Service
public class WeatherServiceImpl implements WeatherService {

    @Override
    public ResultJson<List<JSONObject>> getMonthWeather(String date, String city) {
        ResultJson<List<JSONObject>> weather;
        try {
            weather = WeatherAPI.getWeather(date, city);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResultJson<>(404, null);
        }
        return weather;
    }

    @Override
    public ResultJson<List<JSONObject>> getFiveDayWeather(String date, String city) {
        return null;
    }
}
