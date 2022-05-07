package com.threeonetwo.weatherservice.utils;

/**
 * @Class: WeatherAPI
 * @Author: Wei Junwei
 * @Time: 21:42 2022/5/6
 * @XiDianUniversity
 * @Description:
 */
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.text.SimpleDateFormat;
import java.util.*;
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;

import static com.threeonetwo.weatherservice.utils.KeyUtils.calcAuthorization;
import static com.threeonetwo.weatherservice.utils.KeyUtils.urlencode;

public class WeatherAPI {

    public static ResultJson<List<JSONObject>> getWeather(String date, String city) throws Exception {
        //云市场分配的密钥Id
        String secretId = "AKIDC4rWa0qvkc502e5Kc5Hlr6krMGqjjlky9tpx";
        //云市场分配的密钥Key
        String secretKey = "c5Wi8iTJTKm1gv85sU0liRiKm95834LhogcPypbn";
        String source = "market";

        Calendar cd = Calendar.getInstance();
        SimpleDateFormat sdf = new SimpleDateFormat("EEE, dd MMM yyyy HH:mm:ss 'GMT'", Locale.US);
        sdf.setTimeZone(TimeZone.getTimeZone("GMT"));
        String datetime = sdf.format(cd.getTime());
        // 签名
        String auth = calcAuthorization(source, secretId, secretKey, datetime);
        // 请求方法
        String method = "GET";
        // 请求头
        Map<String, String> headers = new HashMap<String, String>();
        headers.put("X-Source", source);
        headers.put("X-Date", datetime);
        headers.put("Authorization", auth);

        // 查询参数
        Map<String, String> queryParams = new HashMap<String, String>();
        queryParams.put("area", city);
        queryParams.put("areaid","");
        queryParams.put("month", date);
        // body参数
        Map<String, String> bodyParams = new HashMap<String, String>();

        // url参数拼接
        String url = "https://service-iw45ygyx-1255468759.ap-beijing.apigateway.myqcloud.com/release/idhistory";
        if (!queryParams.isEmpty()) {
            url += "?" + urlencode(queryParams);
        }

        BufferedReader in = null;
        try {
            URL realUrl = new URL(url);
            HttpURLConnection conn = (HttpURLConnection) realUrl.openConnection();
            conn.setConnectTimeout(5000);
            conn.setReadTimeout(5000);
            conn.setRequestMethod(method);

            // request headers
            for (Map.Entry<String, String> entry : headers.entrySet()) {
                conn.setRequestProperty(entry.getKey(), entry.getValue());
            }

            // request body
            Map<String, Boolean> methods = new HashMap<>();
            methods.put("POST", true);
            methods.put("PUT", true);
            methods.put("PATCH", true);
            Boolean hasBody = methods.get(method);
            if (hasBody != null) {
                conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");

                conn.setDoOutput(true);
                DataOutputStream out = new DataOutputStream(conn.getOutputStream());
                out.writeBytes(urlencode(bodyParams));
                out.flush();
                out.close();
            }

            // 定义 BufferedReader输入流来读取URL的响应
            in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String line;
            String result = "";
            while ((line = in.readLine()) != null) {
                result += line;
            }

            /**
             * 从原始数据中获得JSONObject
             * 得到showapi_res_body部分
             */
            JSONObject resultJson = JSON.parseObject(result);
            JSONObject showapi_res_body = JSON.parseObject(resultJson.get("showapi_res_body").toString());
            String list = showapi_res_body.get("list").toString();
            /**
             * 字符串分割，获得当前月份的天气数据
             */
            int length = list.length();
            list = list.substring(1, length - 1);
            String[] jsonList = list.split("},");
            List<JSONObject> jsonObjects = new ArrayList<>();
            for (String s : jsonList) {
                if (s.charAt(s.length() - 1) != '}') {
                    JSONObject object = JSON.parseObject(s + "}");
                    jsonObjects.add(object);
                } else {
                    jsonObjects.add(JSON.parseObject(s));
                }
            }
            for (JSONObject jsonObject : jsonObjects) {
                System.out.println(jsonObject);
            }
            return new ResultJson<>(200 , jsonObjects);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResultJson<>(500 , null);
        } finally {
            try {
                if (in != null) {
                    in.close();
                }
            } catch (Exception e2) {
                e2.printStackTrace();
            }
        }
    }
}
