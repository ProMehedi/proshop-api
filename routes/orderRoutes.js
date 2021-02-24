import express from 'express'
import {
  addNewOrder,
  getOrderById,
  updateOrderToPaid,
} from '../controllers/orderController.js'
import { protect } from '../middleware/authMiddleware.js'

const router = express.Router()

// Create New Order
router.route('/').post(protect, addNewOrder)

// Get A Order By ID
router.route('/:id').get(protect, getOrderById)

// Get A Order By ID
router.route('/:id/pay').put(protect, updateOrderToPaid)

export default router
