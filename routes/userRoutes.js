import express from 'express'
import {
  authUser,
  getUserProfile,
  getUsers,
} from '../controllers/userController.js'
import { protect } from '../middleware/authMiddleware.js'

const router = express.Router()

// Fetch All Products
router.route('/').get(getUsers)

// Authenticate User & Get Token
router.route('/login').post(authUser)

// Get User Profile
router.route('/profile').get(protect, getUserProfile)

export default router
