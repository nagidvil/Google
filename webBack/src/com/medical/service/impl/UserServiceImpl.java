package com.medical.service.impl;

import com.medical.dao.UserDao;
import com.medical.dao.impl.UserDaoImpl;
import com.medical.entity.User;
import com.medical.service.UserService;

public class UserServiceImpl implements UserService{
	
	private UserDao userDao=new UserDaoImpl();

	@Override
	public void registUser(User user) {
		userDao.saveUser(user);
	}

	@Override
	public User login(User user) {
		return userDao.queryUserByUsernameAndPassword(user.getUsername(), user.getPassword());
	}

	@Override
	public boolean existsUsername(String username) {
		if(userDao.queryUserByUsername(username)==null)
			return false;
		return true;
	}

}
