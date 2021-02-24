import mongoose from 'mongoose'
import colors from 'colors'
import dotenv from 'dotenv'
import connectDB from './config/db.js'
import Order from './models/orderModel.js'
import Product from './models/productModel.js'
import User from './models/userModel.js'
import users from './data/users.js'
import products from './data/products.js'

// Execute Dotenv
dotenv.config()

// Connect MongoDB
connectDB()

const importData = async () => {
  try {
    // Eress All Tables from Database
    await Order.deleteMany()
    await Product.deleteMany()
    await User.deleteMany()

    // Store All Data
    const sampleUser = await User.insertMany(users)
    const adminUser = sampleUser[0].id
    const sampleProducts = products.map((product) => {
      return { ...product, user: adminUser }
    })

    // Insert Sample Data to MongoDB
    await Product.insertMany(sampleProducts)
    console.log('Sample Data Imported!'.green.inverse)
    process.exit()
  } catch (error) {
    console.error(`${error}`.red.inverse)
    process.exit()
  }
}

const destroyData = async () => {
  try {
    // Eress All Tables from Database
    await Order.deleteMany()
    await Product.deleteMany()
    await User.deleteMany()

    console.log('All Data Destroyed!'.red.inverse)
    process.exit()
  } catch (error) {
    console.error(`${error}`.red.inverse)
    process.exit()
  }
}

if (process.argv[2] === '-d') {
  destroyData()
} else {
  importData()
}
