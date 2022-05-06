package com.threeonetwo.weatherservice.utils;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @Class: ResultJson
 * @Author: Wei Junwei
 * @Time: 21:35 2022/5/6
 * @XiDianUniversity
 * @Description:
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
public class ResultJson<T> {

    /**
     * 定义返回JSON格式
     */
    private Integer err_code;

    private T data;

}
