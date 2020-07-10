package com.medical.dao.impl;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;

import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.BeanHandler;
import org.apache.commons.dbutils.handlers.BeanListHandler;
import org.apache.commons.dbutils.handlers.ScalarHandler;

import com.medical.utils.JdbcUtils;




public abstract class BaseDao{

	private QueryRunner queryRunner=new QueryRunner();
	
	
	public int update(String sql,Object...args){
		
		Connection conn=JdbcUtils.getConnection();
		try {
			return queryRunner.update(conn, sql, args);
		} catch (SQLException e) {
			e.printStackTrace();
		}finally {
			JdbcUtils.close(conn);
		}
		return -1;
	}
	
	public<T> T queryForOne(Class<T> type,String sql,Object...args){
		Connection conn=JdbcUtils.getConnection();
		try {
			return queryRunner.query(conn, sql, new BeanHandler<T>(type), args);
		} catch (SQLException e) {
			e.printStackTrace();
		}finally {
			JdbcUtils.close(conn);
		}
		return null;
	}
	
	public<T> List<T> queryForList(Class<T> type,String sql,Object...args){
		Connection conn=JdbcUtils.getConnection();
		try {
			return queryRunner.query(conn, sql, new BeanListHandler<T>(type), args);
		} catch (SQLException e) {
			e.printStackTrace();
		}finally {
			JdbcUtils.close(conn);
		}
		return null;
	}
	
	 public Object queryForSingleValue(String sql, Object... args){

	        Connection conn = JdbcUtils.getConnection();

	        try {
	            return queryRunner.query(conn, sql, new ScalarHandler(), args);
	        } catch (Exception e) {
	            e.printStackTrace();
	        } finally {
	            JdbcUtils.close(conn);
	        }
	        return null;

	 }
	 
	 public int setIncreaseId(String table_name,String column_name,Object...args) {
		 Connection conn = JdbcUtils.getConnection();	 
		 try {
			String sql1="ALTER TABLE `"+table_name+"` DROP `"+column_name+"`"; 
			if(queryRunner.update(conn, sql1, args)==-1) return -1;
			String sql2="ALTER TABLE `"+table_name+"` ADD `"+column_name+"` int NOT NULL FIRST";
			if(queryRunner.update(conn, sql2, args)==-1) return -1;
			String sql3="ALTER TABLE `"+table_name+"` MODIFY COLUMN `"+column_name+"` int NOT NULL AUTO_INCREMENT,ADD PRIMARY KEY("+column_name+")";
			if(queryRunner.update(conn, sql3, args)==-1) return -1;
		} catch (SQLException e) {
			e.printStackTrace();
		}
		 
		 return 0;
	 }
}
