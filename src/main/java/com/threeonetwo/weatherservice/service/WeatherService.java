package com.threeonetwo.weatherservice.service;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.threeonetwo.weatherservice.utils.ResultJson;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @Class: WeatherService
 * @Author: Wei Junwei
 * @Time: 21:39 2022/5/6
 * @XiDianUniversity
 * @Description:
 */
@Service
public interface WeatherService {
    /**
     * 获得该月全部天气数据
     */
    public ResultJson<List<JSONObject>> getMonthWeather(String date, String city);

    /**
     * 获得当前日期前5天天气数据
     */
    public ResultJson<List<JSONObject>> getFiveDayWeather(String date, String city);

}
