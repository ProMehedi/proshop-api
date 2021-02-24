import asyncHandler from 'express-async-handler'
import User from '../models/userModel.js'
import generateToken from '../utils/genarateToken.js'

// @desc    Fetch All Users
// @route   GET /api/v1/users
// @access  Public
export const getUsers = asyncHandler(async (req, res) => {
  const userList = await User.find().select('-password')

  if (userList) {
    res.status(201).json(userList)
  } else {
    res.status(404)
    throw new Error('No User Found!')
  }
})

// @desc    Auth User & Get Token
// @route   GET /api/v1/users/login
// @access  Public
export const authUser = asyncHandler(async (req, res) => {
  const { email, password } = req.body
  const user = await User.findOne({ email })

  if (user) {
    if (user && user.mathPassword(password)) {
      const token = generateToken(user._id)
      res.status(201).send({
        name: user.name,
        email: user.email,
        isAdmin: user.isAdmin,
        token,
      })
    } else {
      res.status(400).send('Email or Password Wrong!')
    }
  } else {
    res.status(404)
    throw new Error('User not Found!')
  }
})
