import express from 'express'
import {
  authUser,
  deleteUser,
  getUserById,
  getUserProfile,
  getUsers,
  registerUser,
  updateUserById,
  updateUserProfile,
} from '../controllers/userController.js'
import { isAdminUser, isLogin } from '../middleware/authMiddleware.js'

const router = express.Router()

// Get User Profile
router
  .route('/profile')
  .get(isLogin, getUserProfile)
  .put(isLogin, updateUserProfile)

// Fetch All Users
router.route('/').post(registerUser).get(isLogin, isAdminUser, getUsers)

// Fetch & Delete A User By Id
router
  .route('/:id')
  .get(isLogin, isAdminUser, getUserById)
  .delete(isLogin, isAdminUser, deleteUser)
  .put(isLogin, isAdminUser, updateUserById)

// Authenticate User & Get Token
router.route('/login').post(authUser)

export default router
