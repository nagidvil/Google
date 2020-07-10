package com.medical.socket;



import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;
import org.apache.commons.text.StringEscapeUtils;
import org.json.JSONObject;

import com.medical.utils.SocketUtils;

public class statistic_function {
	//age
	//**
	public static JSONObject age_allnumber_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		String command1="get_age_allnumber";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**
	public static JSONObject age_addnumber_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_age_addnumber";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**
	public static JSONObject age_results_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_age_results";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**
	public static JSONObject age_picture_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_age_picture";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
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
	
	
	
	//year
	//**
	public static JSONObject time_allnumber_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_time_allnumber";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**
	public static JSONObject time_addnumber_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_time_addnumber";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**
	public static JSONObject year_results_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_year_results";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**
	public static JSONObject year_picture_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_year_picture";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
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
	
	
	
	
	//month
	
	//*???????????????调好了
	public static JSONObject month2019_results_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_month2019_results";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//*??????????????调好了
	public static JSONObject month2020_results_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_month2020_results";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**
	public static JSONObject month2019_picture_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_month2019_picture";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
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
	//**
	public static JSONObject month2020_picture_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_month2020_picture";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
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
	
	
	
	//day
	
	//**
	public static JSONObject day_results_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_day_results";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**
	public static JSONObject day_picture_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_day_picture";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
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
	
	
	
	//country
	//**
	public static JSONObject country_allnumber_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_country_allnumber";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**已解决
	public static JSONObject country_addnumber_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_country_addnumber";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**
	public static JSONObject country_results_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_country_results";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**
	public static JSONObject country_picture_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_country_picture";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
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
	
	
	
	
	//province
	//**
	public static JSONObject province_allnumber_fuction(String province) throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_province_allnumber";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		String command2= province;
		byte [] com2=SocketUtils.process_command(command2);
		outputStream.write(com2);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**已修正
	public static JSONObject province_addnumber_fuction(String province) throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_province_addnumber";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		String command2=province;
		byte [] com2=SocketUtils.process_command(command2);
		outputStream.write(com2);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**
	public static JSONObject province_results_fuction(String province) throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_province_results";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		String command2=province;
		byte [] com2=SocketUtils.process_command(command2);
		outputStream.write(com2);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//*代码有问题，显示不完全，最下面横坐标没有显示
	public static JSONObject province_picture_fuction(String province) throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_province_picture";
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
	
	
	
	//city
	//**
	public static JSONObject city_allnumber_fuction(String city) throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_city_allnumber";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		String command3=city;
		byte [] com3=SocketUtils.process_command(command3);
		outputStream.write(com3);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**
	public static JSONObject city_addnumber_fuction(String city) throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_city_addnumber";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		String command3=city;
		byte [] com3=SocketUtils.process_command(command3);
		outputStream.write(com3);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**
	public static JSONObject city_results_fuction(String city) throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_city_results";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();

		String command3=city;
		byte [] com3=SocketUtils.process_command(command3);
		outputStream.write(com3);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**
	public static JSONObject city_picture_fuction(String city) throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_city_picture";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();

		String command2=city;
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
	
	
	
	
	//name
	//**
	public static JSONObject get_province_allnamelist_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_province_allnamelist";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	//**
	public static JSONObject get_city_allnamelist_fuction() throws Exception{
		String host="39.106.175.112";
		int port=6666;
		Socket socket=new Socket(host,port);
		
		DataOutputStream outputStream=new DataOutputStream(socket.getOutputStream());
		
		String command1="get_city_allnamelist";
		byte [] com1=SocketUtils.process_command(command1);
		outputStream.write(com1);
		outputStream.flush();
		
		DataInputStream inputStream=new DataInputStream(socket.getInputStream());
		
		JSONObject json_info=SocketUtils.receive_json(inputStream);
		socket.close();
		return json_info;
	}
	

}
