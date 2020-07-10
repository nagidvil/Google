package com.medical.socket;


import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.net.Socket;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URLDecoder;
import java.net.URLEncoder;
import java.net.UnknownHostException;
import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.medical.utils.SocketUtils;
import com.medical.utils.WebUtils;

import org.json.JSONObject;
//**
public class get_data_function {
	public static JSONObject getWebData(String webUrl) throws Exception {
		JSONObject ob =dataFromPython("getWebData",webUrl);
		return ob;
	}
	public static JSONObject dataFromPython(String command1,String command2) throws Exception {
		String host = "39.106.175.112";
        int port = 6666;
        Socket socket = new Socket(host, port);
        DataOutputStream outputStream =new DataOutputStream(socket.getOutputStream());//定义向Python发送信息的输出流
        byte [] com1 = SocketUtils.process_command(command1);//将命令转成byte形式
        outputStream.write(com1);//发送命令
        outputStream.flush();//清缓存
        JSONObject json_info = new JSONObject();
        if(command2!="")
    	{
		    byte [] com2 = SocketUtils.process_command(command2);
		    outputStream.write(com2);
		    outputStream.flush();
		    DataInputStream inputStream = new DataInputStream(socket.getInputStream());//接收Python传来的数据
		    json_info =SocketUtils.receive_json(inputStream);
    	}
	    //接收json数据，存到json_info
        socket.close();//关闭和Python服务器连接
        return json_info;
	}
	

	  
	  
}
