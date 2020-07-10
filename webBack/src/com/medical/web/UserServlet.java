package com.medical.web;

import java.io.BufferedReader;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.beanutils.BeanUtils;
import org.json.JSONObject;


import com.google.code.kaptcha.servlet.*;
import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.medical.entity.User;
import com.medical.service.UserService;
import com.medical.service.impl.UserServiceImpl;
import com.medical.utils.WebUtils;

public class UserServlet extends BaseServlet {
	
	private UserService userService=new UserServiceImpl();
    public UserServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

   
   
    private JsonObject getUserJSONState(User loginUser,int state){
    	//将用户信息和状态转换为json对象
    	Gson gson=new Gson();
    	String userJsonStr=gson.toJson(loginUser);
    	JsonObject responseJson = new JsonParser().parse(userJsonStr).getAsJsonObject();
    	responseJson.addProperty("state",state);
    	responseJson.addProperty("msg", "");
    	return responseJson;
    }
    
	protected void login(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("进来了");
		String json = WebUtils.readJSONString(request);
        JSONObject jsonObject = new JSONObject(json);
		String username=jsonObject.getString("username");
		String password=jsonObject.getString("password");
		User verifyUser=new User(null, username, password, null);
		User loginUser = userService.login(verifyUser);
        // 如果等于null,说明登录 失败!
        if (loginUser == null) {
        	System.out.println("登录失败");
        	JsonObject responseJson=getUserJSONState(verifyUser,0);
        	responseJson.addProperty("msg", "用户名或密码错误");
        	response.getWriter().write(responseJson.toString());   
        	
        } else {
            // 登录 成功
        	System.out.println("登录成功");
        	JsonObject responseJson=getUserJSONState(loginUser,1);
        	responseJson.addProperty("msg", "登录成功");
        	response.getWriter().write(responseJson.toString()); 
        }
	}
	protected void logOff(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.getSession().invalidate();
		response.sendRedirect(request.getContextPath());
	}
	protected void regist(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		System.out.println("进来了");
		String json = WebUtils.readJSONString(request);
        JSONObject jsonObject = new JSONObject(json);
		String username=jsonObject.getString("username");
		String password=jsonObject.getString("password");
		String email=jsonObject.getString("email");

		User user=new User(null, username, password, email);
    	//User user=WebUtils.copyParaToBean(request.getParameterMap(), new User());
    	System.out.println(user+"!!!");
		JSONObject responseJSON=new JSONObject();

        // 获取 Session 中的验证码 
      /*
		String token = (String) request.getSession().getAttribute(com.google.code.kaptcha.Constants.KAPTCHA_SESSION_KEY); 
        // 删除 Session 中的验证码 
        request.getSession().removeAttribute(com.google.code.kaptcha.Constants.KAPTCHA_SESSION_KEY); 
        */

        //if (token != null && token.equalsIgnoreCase(code)) {
        	 //if ("abcde".equalsIgnoreCase(code)) {
		
		
            if (userService.existsUsername(username)) {
            	
            	JsonObject responseJson=getUserJSONState(user,0);
            	responseJson.addProperty("msg", "用户名[" + username + "]已存在!");
            	response.getWriter().write(responseJson.toString()); 
            } else {
                //可用
                //调用Service保存到数据库
            	//User user=WebUtils.copyParaToBean(request.getParameterMap(), new User());
            	System.out.println("注册成功");
                userService.registUser(user);//new User(null, username, password, email,flag)
                JsonObject responseJson=getUserJSONState(user,1);
                responseJson.addProperty("msg", "注册成功");
            	response.getWriter().write(responseJson.toString()); 
  
                
            }
	}
	

}
