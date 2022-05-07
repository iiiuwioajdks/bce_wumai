package com.threeonetwo.weatherservice;

import com.threeonetwo.weatherservice.utils.KeyUtils;
import com.threeonetwo.weatherservice.utils.WeatherAPI;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class WeatherserviceApplicationTests {

    @Test
    void contextLoads() {

        try {
            WeatherAPI.getWeather("202205", "西安");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
