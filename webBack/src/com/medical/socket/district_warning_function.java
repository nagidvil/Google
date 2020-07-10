package com.medical.socket;



import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;
import org.apache.commons.text.StringEscapeUtils;
import org.json.JSONObject;

import com.medical.utils.SocketUtils;

public class district_warning_function {
	//**
	public static JSONObject area_highgrade_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_area_highgrade";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**
	public static JSONObject area_midgrade_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_area_midgrade";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	
	
	//危急患者
	//*
	public static JSONObject dan_patient_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_dan_patient";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	
	//相似病例
	//*
	public static JSONObject similar_patient_fuction(String s_num) throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_similar_patient";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		String command2=s_num;
		byte [] com2=SocketUtils.process_command(command2);
		outputStream.write(com2);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	
	
	//画图
	
	//年龄
	//**
	public static JSONObject area_age_pic_fuction(String province) throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_area_age_pic";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		String command2=province;
		byte [] com2=SocketUtils.process_command(command2);
		outputStream.write(com2);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		String path_of_pic=SocketUtils.receive_file(inputStream);
		String path_of_pic_re =StringEscapeUtils.unescapeJava(path_of_pic);
		String jsonStr = "{'picture':'"+path_of_pic_re+"'}";
		System.out.println(jsonStr);
		JSONObject jsonObject = new JSONObject(jsonStr);
		socket.close();
		return jsonObject;
	}
	
	//各市
	//**
	public static JSONObject area_city_pic_fuction(String province) throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_area_city_pic";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		String command2=province;
		byte [] com2=SocketUtils.process_command(command2);
		outputStream.write(com2);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		String path_of_pic=SocketUtils.receive_file(inputStream);
		String path_of_pic_re =StringEscapeUtils.unescapeJava(path_of_pic);
		String jsonStr = "{'picture':'"+path_of_pic_re+"'}";
		System.out.println(jsonStr);
		JSONObject jsonObject = new JSONObject(jsonStr);
		socket.close();
		return jsonObject;
	}
	
	//月
	//**
	public static JSONObject area_month_pic_fuction(String province) throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_area_month_pic";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		String command2=province;
		byte [] com2=SocketUtils.process_command(command2);
		outputStream.write(com2);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		String path_of_pic=SocketUtils.receive_file(inputStream);
		String path_of_pic_re =StringEscapeUtils.unescapeJava(path_of_pic);
		String jsonStr = "{'picture':'"+path_of_pic_re+"'}";
		System.out.println(jsonStr);
		JSONObject jsonObject = new JSONObject(jsonStr);
		socket.close();
		return jsonObject;
	}
}
