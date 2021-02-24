import express from 'express'
import { addNewOrder } from '../controllers/orderController.js'
import { protect } from '../middleware/authMiddleware.js'

const router = express.Router()

// Create New Order
router.route('/').post(protect, addNewOrder)

export default router
