import asyncHandler from 'express-async-handler'
import User from '../models/userModel.js'
import generateToken from '../utils/genarateToken.js'

// @desc    Fetch All Users
// @route   GET /api/v1/users
// @access  Private/Admin
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

  if (user && (await user.matchPassword(password))) {
    const token = generateToken(user._id)
    res.json({
      _id: user._id,
      name: user.name,
      email: user.email,
      isAdmin: user.isAdmin,
      token,
    })
  } else {
    res.status(401)
    throw new Error('Email or Password Wrong!')
  }
})

// @desc    Get A User By ID
// @route   GET /api/v1/users/:id
// @access  Private/Admin
export const getUserById = asyncHandler(async (req, res) => {
  const user = await User.findById(req.params.id).select('-password')

  if (user) {
    res.status(201).json(user)
  } else {
    res.status(404)
    throw new Error('User Not Found!')
  }
})

// @desc    Get User Profile
// @route   GET /api/v1/users/profile
// @access  Private
export const getUserProfile = asyncHandler(async (req, res) => {
  const user = await User.findById(req.user._id)

  if (user) {
    res.status(201).json({
      _id: user._id,
      name: user.name,
      email: user.email,
      isAdmin: user.isAdmin,
    })
  } else {
    res.status(404)
    throw new Error('User not Found!')
  }
})

// @desc    Update User Profile
// @route   PUT /api/v1/users/profile
// @access  Private
export const updateUserProfile = asyncHandler(async (req, res) => {
  const user = await User.findById(req.user._id)

  if (user) {
    user.name = req.body.name || user.name
    user.email = req.body.email || user.email
    user.phone = req.body.phone || user.phone
    user.postalCode = req.body.postalCode || user.postalCode
    user.city = req.body.city || user.city
    user.country = req.body.country || user.country
    if (req.body.password) {
      user.password = req.body.password
    }

    const updatedUser = await user.save()

    res.json({
      _id: updatedUser._id,
      name: updatedUser.name,
      email: updatedUser.email,
      phone: updatedUser.phone,
      isAdmin: updatedUser.isAdmin,
      postalCode: updatedUser.postalCode,
      city: updatedUser.city,
      country: updatedUser.country,
      token: generateToken(updatedUser._id),
    })
  } else {
    res.status(404)
    throw new Error('User not Found!')
  }
})

// @desc    Update A User By Id
// @route   PUT /api/v1/users/:id
// @access  Private/Admin
export const updateUserById = asyncHandler(async (req, res) => {
  const user = await User.findById(req.params.id)

  if (user) {
    user.name = req.body.name || user.name
    user.email = req.body.email || user.email
    user.phone = req.body.phone || user.phone
    user.postalCode = req.body.postalCode || user.postalCode
    user.city = req.body.city || user.city
    user.country = req.body.country || user.country
    user.isAdmin = req.body.isAdmin

    const updatedUser = await user.save()

    res.json({
      _id: updatedUser._id,
      name: updatedUser.name,
      email: updatedUser.email,
      phone: updatedUser.phone,
      isAdmin: updatedUser.isAdmin,
      postalCode: updatedUser.postalCode,
      city: updatedUser.city,
      country: updatedUser.country,
    })
  } else {
    res.status(404)
    throw new Error('User not Found!')
  }
})

// @desc    Register New User
// @route   POST /api/v1/users/
// @access  Public
export const registerUser = asyncHandler(async (req, res) => {
  const {
    name,
    email,
    password,
    phone,
    isAdmin,
    postalCode,
    city,
    country,
  } = req.body
  const userExists = await User.findOne({ email })

  if (userExists) {
    res.status(400)
    throw new Error('User already exists!')
  }

  const user = await User.create({
    name,
    email,
    password,
    phone,
    isAdmin,
    postalCode,
    city,
    country,
  })

  if (user) {
    const token = generateToken(user._id)
    res.status(201).send({
      _id: user._id,
      name: user.name,
      email: user.email,
      phone: user.phone,
      isAdmin: user.isAdmin,
      postalCode: user.postalCode,
      city: user.city,
      country: user.country,
      token,
    })
  } else {
    res.status(400)
    throw new Error('Invalid user data!')
  }
})

// @desc    Delete A User by Id
// @route   DELETE /api/v1/users/:id
// @access  Private/Admin
export const deleteUser = asyncHandler(async (req, res) => {
  const user = await User.findById(req.params.id)

  if (user) {
    await user.remove()
    res.status(201).json({ success: true, message: 'User Deleted!' })
  } else {
    res.status(404)
    throw new Error('User Not Found!')
  }
})
