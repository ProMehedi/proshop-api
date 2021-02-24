import express from 'express'
import { authUser, getUsers } from '../controllers/userController.js'

const router = express.Router()

// Fetch All Products
router.route('/').get(getUsers)

// Authenticate User & Get Token
router.route('/login').post(authUser)

export default router
