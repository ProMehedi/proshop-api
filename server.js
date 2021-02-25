import path from 'path'
import express from 'express'
import dotenv from 'dotenv'
import morgan from 'morgan'
import colors from 'colors'
import productRoutes from './routes/productRoutes.js'
import userRoutes from './routes/userRoutes.js'
import orderRoutes from './routes/orderRoutes.js'
import uploadRoutes from './routes/uploadRoutes.js'
import connectDB from './config/db.js'
import * as errorMiddleware from './middleware/errorMiddleware.js'

// Initialize Dotenv
dotenv.config()

// Connect MongoDB
connectDB()

// Initialize The Express
const app = express()

// Initialize Morgan
if (process.env.NODE_ENV === 'development') {
  app.use(morgan('dev'))
}

// Middleware
app.use(express.json())

// Define Variables
const api = process.env.API_URL || '/api/'
const port = process.env.PORT || 5000

app.get('/', (req, res) => {
  res.send('Server is ready!')
})

// Product Routes
app.use(`${api}/products`, productRoutes)

// User Routes
app.use(`${api}/users`, userRoutes)

// Order Routes
app.use(`${api}/orders`, orderRoutes)

// Order Routes
app.use(`${api}/uploads`, uploadRoutes)

// Point the uploads folder
const __dirname = path.resolve()
app.use('/uploads', express.static(path.join(__dirname, '/uploads')))

// Custom Error Handling
app.use(errorMiddleware.notFound)
app.use(errorMiddleware.errorHandler)

// Initialize The Server
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`.yellow.bold)
})
