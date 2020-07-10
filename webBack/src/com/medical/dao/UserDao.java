package com.medical.dao;

import com.medical.entity.User;

public interface UserDao {
	//查询用户名 
	public User queryUserByUsername(String username);
	//保存用户信息
	public int saveUser(User user);
	
	//查询用户名和密码
	public User queryUserByUsernameAndPassword(String username,String password);
}
