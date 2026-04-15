sentry_sdk.init(
	dsn="https://6b84fb268580ba26d7195f78f52ff01c@o4511223693967360.ingest.de.sentry.io/4511223699275856",			# Адрес, на который сервис будет отправлять события (Указан на странице в пункте выше)
	environment="development",
	release="1.0"
)

if __name__ == "__main__":
  division_zero = 1 / 0	