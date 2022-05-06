package com.threeonetwo.weatherservice.controller;

import com.alibaba.fastjson.JSONObject;
import com.threeonetwo.weatherservice.service.WeatherService;
import com.threeonetwo.weatherservice.utils.ResultJson;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * @Class: indexController
 * @Author: Wei Junwei
 * @Time: 21:35 2022/5/6
 * @XiDianUniversity
 * @Description:
 */

@RestController
public class indexController {

    @Autowired
    WeatherService weatherService;

    @GetMapping("/weather/{date}/{city}")
    public ResultJson<List<JSONObject>> weather(@PathVariable(value = "date") String date, @PathVariable(value = "city") String city) {
        ResultJson<List<JSONObject>> monthWeather;
        try {
            monthWeather = weatherService.getMonthWeather(date, city);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResultJson<>(404, null);
        }
        return monthWeather;
    }
}
