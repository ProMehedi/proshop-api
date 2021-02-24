import express from 'express'
import { addNewOrder, getOrderById } from '../controllers/orderController.js'
import { protect } from '../middleware/authMiddleware.js'

const router = express.Router()

// Create New Order
router.route('/').post(protect, addNewOrder)
router.route('/:id').get(protect, getOrderById)

export default router
