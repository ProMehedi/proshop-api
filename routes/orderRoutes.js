import express from 'express'
import {
  addNewOrder,
  getMyOrders,
  getOrderById,
  updateOrderToPaid,
} from '../controllers/orderController.js'
import { protect } from '../middleware/authMiddleware.js'

const router = express.Router()

// Get Login User Orders
router.route('/myorders').get(protect, getMyOrders)

// Get A Order By ID
router.route('/:id').get(protect, getOrderById)

// Create New Order
router.route('/').post(protect, addNewOrder)

// Get A Order By ID
router.route('/:id/pay').put(protect, updateOrderToPaid)

export default router
