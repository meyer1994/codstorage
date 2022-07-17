
export const useMagic = () => {
  const router = useRouter()
  const login = () => router.push('/login')

  const user = useState(() => null)
  const token = useState(() => null)
  const authenticated = useState(() => false)

  return { login, user, token, authenticated }
}
