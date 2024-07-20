<template>
  <v-navigation-drawer
    v-model="localDrawer"
    :mini-variant="miniVariant"
    @update:mini-variant="$emit('update:mini-variant', $event)"
    class="custom-drawer"
    temporary
  >
    <v-list dense>  
      <v-list-item link @click="triggerDialog">
        <v-list-item-icon>
          <v-icon>mdi-account</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Group Member</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 'AppSidebar',
  props: {
    drawer: {
      type: Boolean,
      required: true,
    },
    miniVariant: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      localDrawer: this.drawer,
    };
  },
  watch: {
    drawer(val) {
      this.localDrawer = val;
    },
    localDrawer(val) {
      this.$emit('update:drawer', val);
    },
  },
  methods: {
    triggerDialog() {
      this.$emit('trigger-dialog');
    },
  },
};
</script>

<style scoped>
.custom-drawer {
  background-color: #303d4e;
  color: #98a5a6;
}
</style>
