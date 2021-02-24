import express from 'express'
import {
  authUser,
  deleteUser,
  getUserProfile,
  getUsers,
  registerUser,
} from '../controllers/userController.js'
import { isAdminUser, isLogin } from '../middleware/authMiddleware.js'

const router = express.Router()

// Fetch All Products
router.route('/').post(registerUser).get(isLogin, isAdminUser, getUsers)

// Authenticate User & Get Token
router.route('/login').post(authUser)

// Get User Profile
router.route('/profile').get(isLogin, getUserProfile)

// Fetch All Products
router.route('/:id').delete(isLogin, isAdminUser, deleteUser)

export default router
