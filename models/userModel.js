import mongoose from 'mongoose'

const userSchema = mongoose.Schema(
  {
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    phone: { type: String, default: '' },
    password: { type: String, required: true },
    isAdmin: { type: String, required: true, default: false },
    address: { type: String, default: '' },
    postalCode: { type: String, default: '' },
    city: { type: String, default: '' },
    country: { type: String, default: '' },
  },
  { timestamps: true }
)

// Duplicate the ID field.
userSchema.virtual('id').get(function () {
  return this._id.toHexString()
})

// Ensure virtual fields are serialised.
userSchema.set('toJSON', { virtuals: true })

const User = mongoose.model('User', userSchema)
export default User
