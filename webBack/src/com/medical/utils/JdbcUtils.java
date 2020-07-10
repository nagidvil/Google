package com.medical.utils;

import java.io.InputStream;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.Properties;

import com.alibaba.druid.pool.DruidDataSource;
import com.alibaba.druid.pool.DruidDataSourceFactory;
//import com.alibaba.druid.util.JdbcUtils;

public class JdbcUtils {
	
	private static DruidDataSource dataSource;
	
	static {
		try 
		{
			Properties properties=new Properties();
			InputStream inputStream=JdbcUtils.class.getClassLoader().getResourceAsStream("jdbc.properties");
			properties.load(inputStream);
			dataSource=(DruidDataSource) DruidDataSourceFactory.createDataSource(properties);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static Connection getConnection() {
		

		Connection conn=null;
		try {
			conn=dataSource.getConnection();
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return conn;
	}

	public static void close(Connection conn) {
		if(conn!=null)
		{
			try {
				conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}
	public static void main(String[] args) {
		
	}
	
}
