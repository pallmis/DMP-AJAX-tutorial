
<script>
export default {
  computed: {
    hasToken() {
      return this.$store.getters['auth/hasToken'];
    },
  },
};
</script>
